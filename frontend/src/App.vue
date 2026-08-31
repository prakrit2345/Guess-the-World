<template>
  <router-view @navigate="handleNavigate" />
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function handleNavigate(path) {
  router.push(path)
}
</script>