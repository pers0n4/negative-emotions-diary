<template>
  <q-layout view="hhh lpr fFf">
    <q-header elevated class="bg-indigo-1 text-black">
      <q-toolbar>
        <q-btn flat @click="drawer = !drawer" round dense icon="mdi-menu" />
        <q-toolbar-title>EUNOIA</q-toolbar-title>
        <q-space />

        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn round flat icon="mdi-account" to="/signin">
            <q-tooltip>Account</q-tooltip>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

 <!--메뉴 고정 / 복붙한거라 잘 모름-->
       <q-drawer
        v-model="drawer"
        show-if-above

        :width="230"
        :breakpoint="500"
        bordered
        class="bg-indigo-1"
      >
     
     <!--메뉴 이름-->
      <q-list>
        <q-item clickable to="/main">
          <q-item-section avatar>
            <q-icon name="mdi-home" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Home</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable to="/Wdiary">
          <q-item-section avatar>
            <q-icon name="mdi-book-open-variant" />
          </q-item-section>
          <q-item-section>
            <q-item-label>다이어리 작성</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable to="/Search_diary">
          <q-item-section avatar>
            <q-icon name="mdi-magnify" />
          </q-item-section>
          <q-item-section>
            <q-item-label>다이어리 조회</q-item-label>
          </q-item-section>
        </q-item>
      
        <q-item clickable to="/">
          <q-item-section avatar>
            <q-icon name="mdi-emoticon-neutral-outline" />
          </q-item-section>
          <q-item-section>
            <q-item-label>감정 분석</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable to="/emotions_graph">
          <q-item-section avatar>
            <q-icon name="mdi-chart-bar" />
          </q-item-section>
          <q-item-section>
            <q-item-label>그래프</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
  import { ref } from "vue";

  export default {
    setup() {
      const leftDrawerOpen = ref(false);

      return {
        leftDrawerOpen,
        toggleLeftDrawer() {
          leftDrawerOpen.value = !leftDrawerOpen.value;
        },
      };
    },

    data() {
      return {
        email: "",
        password: "",
      };
    },
  };
</script>