/// <reference lib="webworker" />
import { Serwist, NetworkFirst, ExpirationPlugin } from '@serwist/sw';

declare const self: ServiceWorkerGlobalScope & { __WB_MANIFEST: any };

const serwist = new Serwist({
    precacheEntries: self.__WB_MANIFEST,
    skipWaiting: true,
    clientsClaim: true,
    navigationPreload: true,
    runtimeCaching: [
        {
            matcher: ({ request }: { request: Request }) => request.mode === 'navigate',
            handler: new NetworkFirst({
                cacheName: 'pages',
                plugins: [
                    new ExpirationPlugin({
                        maxEntries: 50,
                    }),
                ],
            }),
        },
        {
            matcher: /.*/,
            handler: new NetworkFirst({
                cacheName: 'others',
                plugins: [
                    new ExpirationPlugin({
                        maxEntries: 500,
                        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
                    }),
                ],
            }),
        },
    ],
});

serwist.addEventListeners();
