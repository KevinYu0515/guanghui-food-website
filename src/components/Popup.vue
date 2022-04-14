<template >
  <transition name="fade">
    <div class="background" v-show="open" >
        <div class="preview-box" >
            <div class="details">
                <span class="title">{{image.Name}}</span>
                <span class="icon fi fi-br-cross"  @click="close"></span>
            </div>
            <div class="image-box">
                <slot />
            </div>
        </div>
      <div class="shadow"></div>
    </div>
  </transition>
</template>

<script>
import { onMounted, onUnmounted } from "vue";
export default {
    props:{
        open:{
            type:Boolean,
            default:true,
        }
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
  data(){
      return{
        imageName:"照片預覽"
      }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/scss/popup.scss"
</style>