import { defineConfig } from 'vite'
import { devtools } from '@tanstack/devtools-vite'
import { tanstackStart } from '@tanstack/react-start/plugin/vite'
import viteReact from '@vitejs/plugin-react'
import viteTsConfigPaths from 'vite-tsconfig-paths'
import { fileURLToPath, URL } from 'url'
import tailwindcss from '@tailwindcss/vite'
import { nitro } from 'nitro/vite'
import { serwist } from '@serwist/vite'

const config = defineConfig({
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  plugins: [
    devtools(),
    nitro(),
    viteTsConfigPaths({
      projects: ['./tsconfig.json'],
    }),
    tailwindcss(),
    tanstackStart(),
    viteReact(),
    serwist({
      swSrc: 'src/sw.ts',
      swDest: 'sw.js',
      globPatterns: ['**/*'],
      globDirectory: 'dist',
      injectionPoint: 'self.__WB_MANIFEST',
      rollupFormat: 'iife',

      devOptions: {
        enabled: true,
      },
    })
  ],
})

export default config
