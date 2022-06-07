<template>
  <q-page class="row justify-center items-center">
    <div class="column col-lg-3 col-md-4 col-sm-6">
      <q-card square bordered class="shadow-24">
        <q-card-section>
          <h4 class="text-h5 q-my-md">Sign in</h4>
        </q-card-section>
        <q-card-section>
          <q-form class="q-gutter-md">
            <q-input outlined v-model="email" type="email" label="Email">
              <template v-slot:prepend><q-icon name="mdi-email" /></template>
            </q-input>
            <q-input
              outlined
              v-model="password"
              type="password"
              label="Password"
            >
              <template v-slot:prepend><q-icon name="mdi-lock" /></template>
            </q-input>
          </q-form>
        </q-card-section>
        <q-card-actions class="q-px-md q-mb-md">
          <q-btn
            flat
            color="primary"
            label="Create account"
            no-caps
            to="/signup"
            class="text-bold"
          />
          <q-space />
          <q-btn
            unelevated
            color="primary"
            label="Next"
            no-caps
            padding="xs md"
            class="text-bold"
            @click="signin"
          />
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { useQuasar } from "quasar";
import { defineComponent } from "vue";
import { mapActions } from "vuex";

export default defineComponent({
  name: "SignInPage",
  setup() {
    const $q = useQuasar();

    return {
      showLoginFailNotification() {
        $q.notify({
          color: "negative",
          textColor: "white",
          message: "로그인 실패",
        });
      },
    };
  },
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapActions("auth", ["login"]),
    async signin() {
      const { email, password } = this;

      try {
        await this.login({
          username: email,
          password,
        });

        this.$router.push({ name: "DiaryRead" });
      } catch (error) {
        this.showLoginFailNotification();
      }
    },
  },
});
</script>
