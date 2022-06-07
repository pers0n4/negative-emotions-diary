<template>
  <q-page class="row justify-center items-center q-px-lg">
    <div class="column">
      <q-chat-message
        text-html
        class="self-start"
        :text="[`<h5 class='no-margin'>오늘 하루는 무슨 일이 있었나요?</h5>`]"
      />
      <q-chat-message text-html sent class="self-stretch" size="12">
        <q-editor
          v-model="editor"
          :toolbar="[
            ['bold', 'italic', 'strike', 'underline'],
            ['undo', 'redo'],
          ]"
        />
      </q-chat-message>

      <q-space class="q-my-sm" />

      <q-chat-message
        class="self-start"
        text-html
        :text="[`<h5 class='no-margin'>지금 감정은 어떤가요?</h5>`]"
      />
      <q-chat-message text-html sent class="self-end">
        <div class="q-gutter-xs">
          <q-chip
            v-model:selected="chip.selected"
            v-for="chip in chips"
            :key="chip.key"
            outline
            square
            >{{ chip.name }}</q-chip
          >
        </div>
      </q-chat-message>

      <q-btn color="primary" label="저장" class="q-mt-md" @click="save" />
    </div>
  </q-page>
</template>

<script>
import { ref, reactive } from "vue";

export default {
  setup() {
    const chips = reactive([
      { key: "Hostile", name: "적대감", selected: false },
      { key: "Irritable", name: "짜증", selected: false },
      { key: "Ashamed", name: "부끄럼", selected: false },
      { key: "Guilty", name: "죄책감", selected: false },
      { key: "Distressed", name: "괴로움", selected: false },
      { key: "Upset", name: "화", selected: false },
      { key: "Scared", name: "겁", selected: false },
      { key: "Afraid", name: "두려움", selected: false },
      { key: "Jittery", name: "조바심", selected: false },
      { key: "Nervous", name: "불안", selected: false },
    ]);

    return {
      editor: ref(""),
      chips,
    };
  },
  methods: {
    save() {
      this.$router.push({ name: "DiaryRead" });
    },
  },
};
</script>
