import { defineConfig } from 'vite'
import { devtools } from '@tanstack/devtools-vite'
import { tanstackStart } from '@tanstack/react-start/plugin/vite'
import viteReact from '@vitejs/plugin-react'
import viteTsConfigPaths from 'vite-tsconfig-paths'
import { fileURLToPath, URL } from 'url'
import tailwindcss from '@tailwindcss/vite'
import { nitro } from 'nitro/vite'
import { serwist } from '@serwist/vite'
import { copyFileSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'

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
      globDirectory: '.output/public',
      devOptions: {
        enabled: true,
      },
    }),
    // Custom plugin to copy sw.js to .output/public after build
    {
      name: 'copy-sw-to-output',
      closeBundle() {
        try {
          const swSource = join(process.cwd(), 'dist', 'sw.js')
          const swDest = join(process.cwd(), '.output', 'public', 'sw.js')
          mkdirSync(join(process.cwd(), '.output', 'public'), { recursive: true })
          copyFileSync(swSource, swDest)
          console.log('✓ Copied sw.js to .output/public/')
        } catch (error) {
          const errorMessage = error instanceof Error ? error.message : String(error)
          console.warn('⚠ Could not copy sw.js:', errorMessage)
        }
      },
    },
  ],
})

export default config
