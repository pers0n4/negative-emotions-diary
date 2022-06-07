<template>
  <q-page class="row justify-center items-center q-px-lg">
    <div class="column col-xs-12 col-sm-10 col-md-8">
      <q-chat-message
        text-html
        class="self-start"
        :text="[`<h5 class='no-margin'>오늘 하루는 무슨 일이 있었나요?</h5>`]"
      />
      <q-editor
        v-model="editor"
        :toolbar="[
          ['bold', 'italic', 'strike', 'underline'],
          ['undo', 'redo'],
        ]"
      />

      <q-space class="q-my-sm" />

      <q-chat-message
        class="self-start"
        text-html
        :text="[`<h5 class='no-margin'>지금 감정은 어떤가요?</h5>`]"
      />
      <q-select v-model="selectModel" :options="emotions" outlined />

      <q-btn color="primary" label="저장" class="q-mt-md" @click="save" />
    </div>
  </q-page>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const emotions = [
      { label: "적대감", value: "Hostile" },
      { label: "짜증", value: "Irritable" },
      { label: "부끄럼", value: "Ashamed" },
      { label: "죄책감", value: "Guilty" },
      { label: "괴로움", value: "Distressed" },
      { label: "화", value: "Upset" },
      { label: "겁", value: "Scared" },
      { label: "두려움", value: "Afraid" },
      { label: "조바심", value: "Jittery" },
      { label: "불안", value: "Nervous" },
    ];

    return {
      editor: ref(""),
      selectModel: ref(null),
      emotions,
    };
  },
  methods: {
    save() {
      this.$router.push({ name: "DiaryRead" });
    },
  },
};
</script>
