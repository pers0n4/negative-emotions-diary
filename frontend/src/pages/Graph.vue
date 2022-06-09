<template>
  <q-page class="column">
    <v-chart class="chart" :option="option" autoresize />
  </q-page>
</template>

<script>
import { BarChart } from "echarts/charts";
import { GridComponent } from "echarts/components";
import { use } from "echarts/core";
import { SVGRenderer } from "echarts/renderers";
import { computed, ref } from "vue";
import VChart, { INIT_OPTIONS_KEY } from "vue-echarts";
import { axios } from "../plugins/axios";

use([SVGRenderer, BarChart, GridComponent]);

export default {
  components: {
    VChart,
  },
  provide: {
    [INIT_OPTIONS_KEY]: {
      renderer: "svg",
    },
  },
  setup() {
    const affects = ref([]);
    function fetchAffects() {
      axios.get("/statistics/affects").then((response) => {
        affects.value = Object.entries(response.data).sort(
          (a, b) => a[1].length - b[1].length,
        );
        console.log(affects.value);
      });
    }
    fetchAffects();

    const option = computed(() => ({
      xAxis: {
        type: "category",
        data: affects.value.map(([key]) => key),
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          data: affects.value.map(([, value]) => value.length),
          type: "bar",
        },
      ],
    }));

    return {
      option,
    };
  },
};
</script>

<style scoped>
.chart {
  height: 95vh;
}
</style>
