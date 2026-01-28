import { Scripts, createRootRoute, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'
import { Header } from '../components/Header'
import { ThemeScript } from '../components/ThemeScript'
import { GlobalBreadcrumbs } from '../components/GlobalBreadcrumbs'

import '../styles.css'

export const Route = createRootRoute({
  head: () => ({
    meta: [
      {
        charSet: 'utf-8',
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        title: "Don't Compete",
      },
    ],
    links: [
      // { rel: 'stylesheet', href: appCss },
      {
        rel: 'manifest',
        href: '/manifest.json',
      },
    ],
  }),
  component: () => {
    // Register Service Worker
    if (typeof window !== 'undefined' && 'serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js');
      });
    }

    return (
      <>
        <ThemeScript />
        <Header />
        <GlobalBreadcrumbs />
        <Outlet />
        <Scripts />
        <TanStackRouterDevtools />
      </>
    )
  }
})
