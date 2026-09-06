<script setup>
import axios from 'axios'
import { ref, onBeforeUnmount } from 'vue'
import { Viewer } from 'mapillary-js'
import { LMap, LTileLayer, LMarker } from '@vue-leaflet/vue-leaflet'

import 'leaflet/dist/leaflet.css'
import 'mapillary-js/dist/mapillary.css'

const viewerContainer = ref(null)
const viewer = ref(null)

const imageLocation = ref(null)
const loading = ref(false)

const mapCenter = ref([27.7172, 85.3240])

const getImages = async () => {
  try {
    loading.value = true

    const response = await axios.get(
      'https://graph.mapillary.com/images',
      {
        params: {
          access_token: import.meta.env.VITE_MAPILLARY_TOKEN,

          fields:
            'id,computed_geometry,thumb_1024_url,sequence',

          bbox: '-73.9850,40.7480,-73.9840,40.7490',

          limit: 10
        }
      }
    )

    console.log(response.data)

    const images = response.data.data

    if (!images || images.length === 0) {
      console.log('No Mapillary images found')
      return
    }

    
    const randomImage =
      images[Math.floor(Math.random() * images.length)]

    console.log('Selected image:', randomImage)

  
    const [longitude, latitude] =
      randomImage.computed_geometry.coordinates

    imageLocation.value = [latitude, longitude]

    mapCenter.value = [latitude, longitude]

    
    if (viewer.value) {
      viewer.value.remove()
      viewer.value = null
    }

    
    viewer.value = new Viewer({
      accessToken: import.meta.env.VITE_MAPILLARY_TOKEN,

      container: viewerContainer.value,

      imageId: randomImage.id
    })

    viewer.value.on(
      'load',
      () => {
        console.log('Mapillary viewer loaded')
      }
    )

  } catch (error) {
    console.error(error)
    console.log(error.response?.data)

  } finally {
    loading.value = false
  }
}



onBeforeUnmount(() => {
  if (viewer.value) {
    viewer.value.remove()
    viewer.value = null
  }
})
</script>


<template>

  <div class="pagewrapper">


    <div
      ref="viewerContainer"
      class="streetview"
    >
      <div
        v-if="!viewer"
        class="placeholder"
      >
     
      </div>
    </div>


   

    <button
      class="get-image"
      @click="getImages"
      :disabled="loading"
    >
      {{ loading ? 'Loading...' : 'Get Street View' }}
    </button>



    <div class="mapcontainer">

      <LMap
        :zoom="16"
        :center="mapCenter"
      >

        <LTileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <LMarker
          v-if="imageLocation"
          :lat-lng="imageLocation"
        />

      </LMap>

    </div>

  </div>

</template>


<style scoped>

.pagewrapper {
  position: relative;

  width: 100%;
  height: 100vh;

  overflow: hidden;

  background: #222;
}


/* Mapillary viewer */

.streetview {
  width: 100%;
  height: 100%;

  position: absolute;
  inset: 0;
}



.placeholder {
  position: absolute;

  top: 50%;
  left: 50%;

  transform: translate(-50%, -50%);

  color: white;

  font-size: 24px;
}




.get-image {
  position: absolute;

  top: 20px;
  left: 20px;

  z-index: 1000;

  padding: 12px 20px;

  border: none;
  border-radius: 8px;

  background: white;

  font-size: 16px;

  cursor: pointer;
}

.get-image:disabled {
  cursor: wait;
  opacity: 0.7;
}



.mapcontainer {
  position: absolute;

  bottom: 20px;
  right: 20px;

  width: 300px;
  height: 300px;

  z-index: 1000;

  border: 3px solid white;
  border-radius: 10px;

  overflow: hidden;

  box-shadow:
    0 4px 15px rgba(0, 0, 0, 0.5);
}

</style>