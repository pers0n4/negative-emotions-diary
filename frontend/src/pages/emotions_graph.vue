<template>
  <div class="q-pa-md">
    <div>
      <q-splitter v-model="splitterModel" style="height: 650px">
        <template v-slot:before>
          <div class="q-pa-xs">
            <h5><q-icon name="mdi-calendar-minus"></q-icon> 날짜 선택</h5>
          </div>
          <div class="q-pa-md" style="max-width: 1000px">
            <div class="q-gutter-md">
              <q-select v-model="model" :options="options" label="Year" />
              <q-select v-model="model1" :options="options1" label="Month" />
              <q-select v-model="model2" :options="options2" label="Day" />
            </div>
          </div>
        </template>

        <template v-slot:after>
          <div class="q-pa-md">
            <div class="text-h5 q-pa-md">감정 그래프</div>
            <div class="q-my-md">
              <div class="q-pa-md row items-start q-gutter-md">
                <q-card class="my-card">
                  <q-card-section> 그래프 넣어주세요 </q-card-section>
                </q-card>
              </div>
            </div>
          </div>
        </template>
      </q-splitter>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  data() {},
  setup() {
    return {
      splitterModel: ref(30), // start at 50%
      model: ref(null),
      options: [
        "2022",
        "2021",
        "2020",
        "2019",
        "2018",
        "2017",
        "2016",
        "2015",
        "2014",
        "2013",
        "2012",
        "2011",
        "2010",
        "2009",
        "2008",
        "2007",
        "2006",
        "2005",
        "2004",
        "2003",
        "2002",
        "2001",
        "2000",
        "1999",
        "1989",
        "1979",
        "1969",
        "1959",
        "1949",
        "1939",
        "1929",
        "1919",
        "1910",
        "1909",
        "1908",
        "1907",
        "1906",
        "1905",
        "1904",
        "1903",
        "1902",
        "1901",
        "1900",
      ],
      model1: ref(null),
      options1: [
        "1월",
        "2월",
        "3월",
        "4월",
        "5월",
        "6월",
        "7월",
        "8월",
        "9월",
        "10월",
        "11월",
        "12월",
      ],
      model2: ref(null),
      options2: [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
      ],
    };
  },
};
</script>
