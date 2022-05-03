<template>
  <transition name="fade">
    <div class="background" v-show="open">
      <div class="preview-box">
        <div class="details">
          <slot name="imageName"
            ><span class="title">{{ imageName }}</span></slot
          >
          <img class="icon" @click=close :src="require('@/assets/icon/cross.png')">
        </div>
        <div class="image-box">
          <slot name="img"></slot>
        </div>
      </div>
      <div class="shadow"></div>
    </div>
  </transition>
</template>

<script>
import { onMounted, onUnmounted } from "vue";
export default {
  props: {
    open: {
      type: Boolean,
      default: true,
    },
  },
  setup(_, { emit }) {
    const close = () => {
      emit("close");
    };
    const handleKeyup = (event) => {
      if (event.keyCode === 27) {
        close();
      }
    };

    onMounted(() => document.addEventListener("keyup", handleKeyup));
    onUnmounted(() => document.removeEventListener("keyup", handleKeyup));

    return { close };
  },
  data() {
    return {
      imageName: "照片:p",
    };
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/popup.scss";
</style>
