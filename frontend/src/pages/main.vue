<template>
<div class="row" id = "back">
  <div class="col-8" id = "main_column">
       
       <div class="column" style="height: 525px"> 
          <div class="q-pa-md">
          <div class="col" id = "diary_search">
           
           <q-toolbar class="bg-indigo-4 text-white rounded-borders">
            <q-btn round dense flat icon="mdi-book-open-variant" />
            <span>다이어리 검색</span>
        <q-space />

        <q-input dark dense standout v-model="search" filled type="search" style="width: 500px">
          <template v-slot:append>
            <q-icon v-if="text === ''" name="mdi-magnify" />
            <q-icon v-else class="cursor-pointer" @click="text = ''" name="mdi-magnify" />
          </template>
        </q-input>

      </q-toolbar>

    </div>
  </div>

<div>
         <div class="col-9" id = "diary_write"> 
  
    <q-card class="my-card bg-indigo-2 text-black">
      <q-card-section>
         <q-card-actions vertical align="center"> 
           <q-btn flat to="/Wdiary">
             <q-icon name="mdi-account"/>
             다이어리 작성
             </q-btn>
             </q-card-actions>
      </q-card-section>

    </q-card>             

    <q-card class="my-card bg-indigo-6 text-white">
      <q-card-section>
        <div class="text">다이어리 작성한 글 최신순으로1</div>
      </q-card-section>
    </q-card>

      <q-card class="my-card bg-indigo-5 text-white">
      <q-card-section>
              <div class="text">다이어리 작성한 글 최신순으로2</div>
            </q-card-section>
      </q-card>

      <q-card class="my-card bg-indigo-4 text-white">
      <q-card-section>
              <div class="text">다이어리 작성한 글 최신순으로3</div>
            </q-card-section>
      </q-card>

      <q-card class="my-card bg-indigo-3 text-white">
      <q-card-section>
              <div class="text">다이어리 작성한 글 최신순으로4</div>
            </q-card-section>
      </q-card>

      <q-card class="my-card bg-indigo-2 text-white">
      <q-card-section>
              <div class="text">다이어리 작성한 글 최신순으로5</div>
            </q-card-section>
      </q-card>

         </div>
         </div>
       </div>
  </div>

  <div class="col-4" id = "main_column">
      <div class="column" style="height: 525px">

      <span>감정 그래프</span>
        <div class="col" id="emotion_graph" >  
          그래프를 넣어주세용 
        </div>

        <span>워드클라우드</span>
         <div class="col-3" id="word_cloud" >
           워드클라우드 넣어주세용
         </div>
       </div>
  </div>
</div>

</template>

<script>

export default {
  name: 'App'
}

</script>

<style>

#wirte_btn{
    align-items: center;
}

.my-card{
   width: 650px;
   align-self: center;
    margin-left: auto; 
    margin-right: auto;
}
span{
    text-align: center;
}

#main_column{
    border : 2px double lightblue;
}

#diary_write{
 text-align: left;
}

#emotion_graph{
   border : 2px double red;
}

#word_cloud{
   border : 2px double red;
   }
</style>