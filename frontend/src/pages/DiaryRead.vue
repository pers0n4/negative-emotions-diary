<template>
  <q-page class="row q-pa-md">
    <q-table
      grid
      title="다이어리 목록"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="{ selectModel, filter }"
      :filter-method="filterMethod"
      hide-header
      :rows-per-page-options="[0]"
      class="col-8"
    >
      <template v-slot:top-right>
        <q-select
          clearable
          borderless
          v-model="selectModel"
          :options="selectOption"
        >
          <template v-slot:prepend>
            <q-icon name="mdi-filter" />
          </template>
        </q-select>
        <q-input
          borderless
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search"
        >
          <template v-slot:prepend>
            <q-icon name="mdi-magnify" />
          </template>
        </q-input>
      </template>

      <template v-slot:item="props">
        <div class="q-pa-xs col-xs-12 col-sm-6">
          <q-card>
            <q-card-section v-html="props.row.content" />
            <q-card-section>
              <q-chip>{{ props.row.affect }}</q-chip>
            </q-card-section>
          </q-card>
        </div>
      </template>
    </q-table>

    <div class="col-4">
      <v-chart class="chart" :option="option" autoresize />
      <v-chart class="chart" :option="wordCloud" autoresize />
    </div>
  </q-page>
</template>

<script>
import VChart, { INIT_OPTIONS_KEY } from "vue-echarts";
import { PieChart } from "echarts/charts";
import {
  LegendComponent,
  TitleComponent,
  TooltipComponent,
} from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import { computed, defineComponent, ref } from "vue";
import { axios } from "../plugins/axios";
import "echarts-wordcloud";

use([SVGRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent]);

export default defineComponent({
  components: {
    VChart,
  },
  provide: {
    [INIT_OPTIONS_KEY]: {
      renderer: "svg",
    },
  },
  setup() {
    const rows = ref([]);
    const filter = ref("");
    const selectOption = ref([
      "적대감",
      "짜증",
      "부끄럼",
      "죄책감",
      "괴로움",
      "화",
      "겁",
      "두려움",
      "조바심",
      "불안",
    ]);
    const selectModel = ref("");

    const affects = ref({});
    const option = computed(() => ({
      title: {
        text: "감정 그래프",
        left: "center",
      },
      tooltip: {
        trigger: "item",
      },
      legend: {
        orient: "vertical",
        left: "left",
      },
      series: [
        {
          name: "감정",
          type: "pie",
          radius: "50%",
          data: Object.entries(affects.value).map(([key, value]) => ({
            name: key,
            value: value.length,
          })),
        },
      ],
    }));

    const entities = ref({});
    const wordCloud = computed(() => ({
      series: [
        {
          type: "wordCloud",
          // shape: "circle",
          // keepAspect: false,
          // left: "center",
          // top: "center",
          // width: "70%",
          // height: "80%",
          // right: null,
          // bottom: null,
          // sizeRange: [12, 60],
          // rotationRange: [-90, 90],
          // rotationStep: 45,
          // gridSize: 8,
          // drawOutOfBound: false,
          // layoutAnimation: true,
          textStyle: {
            fontFamily: "sans-serif",
            fontWeight: "bold",
            // color() {},
          },
          emphasis: {
            focus: "self",
          },
          data: Object.entries(entities.value).map(([name, value]) => ({
            name,
            value,
          })),
        },
      ],
    }));

    function fetchDiaries() {
      axios.get("/diaries").then((response) => {
        rows.value = response.data;
      });
    }

    function fetchAffects() {
      axios.get("/statistics/affects").then((response) => {
        affects.value = response.data;
      });
    }

    function fetchEntities() {
      axios.get("/statistics/entities").then((response) => {
        entities.value = response.data;
      });
    }

    fetchDiaries();
    fetchAffects();
    fetchEntities();

    return {
      rows,
      columns: [
        {
          name: "content",
          field: "content",
        },
      ],
      filter,
      filterMethod: (data, { selectModel, filter }) => {
        if (selectModel) {
          data = data.filter((row) => row.affect === selectModel);
        }
        if (filter) {
          data = data.filter((row) =>
            row.content.toLowerCase().includes(filter.toLowerCase()),
          );
        }
        return data;
      },

      selectOption,
      selectModel,

      option,
      wordCloud,
    };
  },
});
</script>

<style lang="sass">
.chart
  height: 400px
</style>
