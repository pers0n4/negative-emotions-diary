<template>
  <q-page class="window-height-50% window-width-20% row justify-center items-center">
    <div class="column col-lg-3 col-md-4 col-sm-6">
      <q-card square bordered class="shadow-24">
        <q-card-section>
          <h4 class="text-h5 q-my-md">Create Account</h4>
        </q-card-section>
        <q-card-section>
          <q-form class="q-gutter-md">
            <q-input
              outlined
              clearable
              v-model="email"
              type="email"
              label="Email"
            >
              <template v-slot:prepend><q-icon name="mdi-email" /></template>
            </q-input>
            <q-input
              outlined
              clearable
              v-model="password"
              type="password"
              label="Password"
            >
              <template v-slot:prepend><q-icon name="mdi-lock" /></template>
            </q-input>
            <q-input
              outlined
              clearable
              v-model="passwordConfirm"
              type="password"
              label="Confirm"
            >
              <template v-slot:prepend><q-icon name="mdi-lock" /></template>
            </q-input>
          </q-form>
        </q-card-section>
        <q-card-actions class="q-px-md q-mb-md">
          <q-btn
            flat
            color="indigo-4"
            label="Sign in instead"
            no-caps
            to="/signin"
            class="text-bold"
          />
          <q-space />
          <q-btn
            unelevated
            color="indigo-4"
            label="Next"
            no-caps
            padding="xs md"
            class="text-bold"
          />
        </q-card-actions>
      </q-card>
    </div>
  </q-page>
</template>

<script>
  export default {
    name: "SignUpPage",
    data() {
      return {
        email: "",
        password: "",
        passwordConfirm: "",
      };
    },
  };
</script>