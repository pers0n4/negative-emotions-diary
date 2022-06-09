<template>
  <div class="q-pa-md">
    <div>
      <q-splitter v-model="splitterModel" style="height: 1000px">
        <template v-slot:before>
          <div class="q-pa-md">
            <div class="q-gutter-md">
              <q-date v-model="date" :events="events" />
            </div>
          </div>
        </template>

        <template v-slot:after>
          <div class="q-pa-md">
            <q-card
              v-for="diary in diaries"
              class="q-mb-sm"
              v-show="show(diary)"
            >
              <q-card-section>
                {{ diary.content }}
              </q-card-section>
            </q-card>
          </div>
        </template>
      </q-splitter>
    </div>
  </div>
</template>

<script>
import { computed, ref } from "vue";
import { axios } from "../plugins/axios";

export default {
  setup() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, "0");
    const day = String(today.getDate()).padStart(2, "0");

    const date = ref(`${year}/${month}/${day}`);

    const diaries = ref([]);
    function fetchDiaries() {
      axios.get("/diaries").then((response) => {
        diaries.value = response.data;
        console.log(
          Object.values(diaries.value).map((diary) =>
            diary.created_at.slice(0, 10).replace(/-/g, "/"),
          ),
        );
      });
    }
    fetchDiaries();

    return {
      date,
      diaries,
      events: computed(() =>
        Object.values(diaries.value).map((diary) =>
          diary.created_at.slice(0, 10).replace(/-/g, "/"),
        ),
      ),
      show: (diary) =>
        diary.created_at.slice(0, 10).replace(/-/g, "/") === date.value,
    };
  },
};
</script>
