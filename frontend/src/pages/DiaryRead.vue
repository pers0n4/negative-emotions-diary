<template>
  <q-page class="row q-pa-md">
    <q-table
      grid
      title="다이어리 목록"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="filter"
      hide-header
      :rows-per-page-options="[0]"
      class="col-8"
    >
      <template v-slot:top-right>
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
          </q-card>
        </div>
      </template>
    </q-table>

    <div class="col-4">
      <v-chart class="chart" :option="option" autoresize />
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
import { useQuasar } from "quasar";
import { computed, defineComponent, ref } from "vue";
import { axios } from "../plugins/axios";

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
    const $q = useQuasar();

    const rows = ref([]);
    const filter = ref("");

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

    function fetchDiaries() {
      axios.get("/diaries").then((response) => {
        rows.value = response.data;
      });
    }

    function fetchAffects() {
      axios.get("/affects").then((response) => {
        affects.value = response.data;
      });
    }

    fetchDiaries();
    fetchAffects();

    return {
      rows,
      columns: [
        {
          name: "content",
          field: "content",
        },
      ],
      filter,

      option,
    };
  },
});
</script>

<style lang="sass">
.chart
  height: 400px

#emotion_graph
  border: 2px double red

#word_cloud
  border: 2px double red
</style>
