<template>
  <q-layout view="hhh lpr fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="mdi-menu" @click="toggleLeftDrawer" />
        <q-toolbar-title>EUNOIA</q-toolbar-title>
        <q-space />

        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn round flat icon="mdi-account" v-if="isAuthenticated">
            <q-tooltip>Account</q-tooltip>
            <q-menu>
              <q-list style="min-width: 100px">
                <q-item clickable @click="signOut">
                  <q-item-section>Logout</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <q-btn round flat icon="mdi-account" to="/signin" v-else>
            <q-tooltip>Account</q-tooltip>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above :width="200" bordered>
      <q-list>
        <q-item clickable :to="{ name: 'DiaryRead' }">
          <q-item-section avatar>
            <q-icon name="mdi-book-open-variant" />
          </q-item-section>
          <q-item-section>
            <q-item-label>다이어리 보기</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable :to="{ name: 'DiaryWrite' }">
          <q-item-section avatar>
            <q-icon name="mdi-pencil" />
          </q-item-section>
          <q-item-section>
            <q-item-label>다이어리 쓰기</q-item-label>
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

        <q-item clickable to="/">
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
import { mapGetters, mapActions } from "vuex";

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
  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
  },
  methods: {
    ...mapActions("auth", ["logout"]),
    signOut() {
      this.logout();
      this.$router.push({ name: "SignIn" });
    },
  },
};
</script>
