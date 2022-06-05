
<template>
  <q-page class="window-height-50% window-width-20% row justify-center items-center">
    <div class="q-pa-md q-gutter-sm" id="write_memo">
       <span class="text" id="text">오늘 oo님의 하루는 어떠셨나요?</span> <br>
         <q-editor
           v-model="editor"      
           flat
           content-class="bg-indigo-1"
           toolbar-text-color="white"
           toolbar-toggle-color="indigo-6"
           toolbar-bg="indigo-3"

           :toolbar="[
            ['bold', 'italic', 'strike', 'underline']
           ]"
         />

     <div class="row justify-end">
       <q-btn
         type="submit"
         :loading="submitting"
          label="Save"
          class="q-mt-md"
          color="indigo-3"
         >
          <template v-slot:loading>
           <q-spinner-facebook />
          </template>
       </q-btn>
     </div>

    <span class="q-pa-md">오늘 내 감정은?</span>
<div class="q-gutter-sm row items-center no-wrap">
    <div class="q-pa-md q-gutter-md">
        <q-btn round color="indigo-2" label="적대감"/>
        <q-btn round color="indigo-2" label="짜증"/>
        <q-btn round color="indigo-2" label="부끄럼"/>
        <q-btn round color="indigo-2" label="죄책감"/>
        <q-btn round color="indigo-2" label="괴로움"/>
        <q-btn round color="indigo-2" label="화"/>
        <q-btn round color="indigo-2" label="겁"/>
        <q-btn round color="indigo-2" label="두려움"/>
        <q-btn round color="indigo-2" label="조바심"/>
        <q-btn round color="indigo-2" label="불안"/>
    </div>
  </div>

<span class="text">오늘 내 기분을 태그해보세요</span>
  <div class="q-pa-md q-gutter-md">
    <div>
      <q-chip q-icon="event"> #적대감 </q-chip>
      <q-chip q-icon="bookmark"> #짜증 </q-chip>
      <q-chip q-icon="alarm"> #부끄럼</q-chip>
      <q-chip q-icon="directions"> #죄책감 </q-chip>
      <q-chip q-icon="directions"> #괴로움 </q-chip>
      <q-chip q-icon="directions"> #화 </q-chip>
      <q-chip q-icon="directions"> #겁 </q-chip>
      <q-chip q-icon="directions"> #두려움 </q-chip>
      <q-chip q-icon="directions"> #조바심 </q-chip>
      <q-chip q-icon="directions"> #불안 </q-chip>
    </div>
  </div>
  </div>
</q-page>
</template>


<script>
import { useQuasar } from 'quasar'
import { ref } from 'vue'

export default {
  setup () {
    const $q = useQuasar()

    return {
      editor: ref(
        '')
    }
  }
}
</script>

<style>

</style>
