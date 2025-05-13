<template>
  <Popup :open="addComment" @close="addComment = !addComment">
      <template #imageName>評論表單</template>
      <template #img>
        <div class="input">
          <label class="nameLabel">Name 評論者名稱</label>
          <input
            type="text"
            class="name"
            placeholder="評論者名稱"
            v-model.trim="commentInput.name"
          />
          <StarRating
            :increment="0.5"
            :max-rating="5"
            inactive-color="#000"
            active-color="#f0f19c"
            :star-size="30"
            :rating="commentInput.star"
          ></StarRating>
          <label class="commentLabel">Comment 評論內容</label>
          <textarea
            rows="2"
            cols="23"
            class="content"
            placeholder="評論內容"
            v-model.trim="commentInput.content"
          ></textarea>
          <div class="buttonBox">
            <button
              type="button"
              class="btn btn-outline-primary delete"
              @click="cancelHandler()"
            >
              Delete
            </button>
            <button
              type="button"
              class="btn btn-outline-warning send"
              @click="submitHandler()"
            >
              Send
            </button>
          </div>
        </div>
      </template>
    </Popup>
</template>

<script>
export default {

}
</script>
