import { useState, useEffect } from 'react'

export interface Topic {
    name: string
    id: string
    slug: string
    md_path: string
    questions: string[]
}

export interface Subject {
    name: string
    id: string
    slug: string
    topics: Topic[]
}

export interface StreamStructure {
    stream: string
    stream_code: string
    subjects: Subject[]
}

export function useStreamStructure(examId: string | undefined, streamId: string | undefined) {
    const [data, setData] = useState<StreamStructure | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<Error | null>(null)

    useEffect(() => {
        if (!streamId) {
            setLoading(false)
            return
        }

        const fetchStructure = async () => {
            try {
                setLoading(true)
                setError(null)
                // Correct path: /assets/gate/<streamId>/structure.json
                const response = await fetch(`/assets/${examId ?? 'gate'}/${streamId}/structure.json`)

                if (!response.ok) {
                    throw new Error(`Stream "${streamId}" not found in exam "${examId}"`)
                }

                const json = await response.json()
                setData(json)
            } catch (err) {
                setError(err instanceof Error ? err : new Error('Failed to load stream'))
                setData(null)
            } finally {
                setLoading(false)
            }
        }

        fetchStructure()
    }, [examId, streamId])

    return { data, loading, error }
}

export function useTheory(examId: string | undefined, streamId: string | undefined, mdPath: string | undefined) {
    const [content, setContent] = useState<string>('')
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<Error | null>(null)

    useEffect(() => {
        if (!streamId || !mdPath) {
            setLoading(false)
            return
        }

        const fetchTheory = async () => {
            try {
                setLoading(true)
                setError(null)
                // Correct path: /assets/<examId>/<streamId>/<mdPath>
                const response = await fetch(`/assets/${examId ?? 'gate'}/${streamId}/${mdPath}`)

                if (!response.ok) {
                    throw new Error(`Theory not found: ${mdPath}`)
                }

                const text = await response.text()
                setContent(text)
            } catch (err) {
                setError(err instanceof Error ? err : new Error('Failed to load theory'))
                setContent('')
            } finally {
                setLoading(false)
            }
        }

        fetchTheory()
    }, [examId, streamId, mdPath])

    return { content, loading, error }
}

// Use Vite's import.meta.glob to find all structure.json files at build/dev time
// This relies purely on the folder structure and returns URLs to the assets
// IMPORTANT: We use { query: '?url', import: 'default' } to get the URL path, NOT the content.
const structureGlobs = import.meta.glob('../../public/assets/*/*/structure.json', { eager: true, query: '?url', import: 'default' })

export function useAvailableStreams(examId: string) {
    const [streams, setStreams] = useState<Array<{ id: string, name: string, code: string }>>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        // Parse the glob results
        // Example key: "../../public/assets/gate/cs/structure.json"

        const foundStreams: Array<{ id: string, name: string, code: string }> = []

        for (const path in structureGlobs) {
            // Check if this path belongs to the current examId
            // We look for /assets/<examId>/<streamId>/structure.json
            // Normalize path separators just in case
            const normalizedPath = path.replace(/\\/g, '/')
            const parts = normalizedPath.split('/')

            // structure.json is last (index N), then streamId (N-1), then examId (N-2)
            // path: ../../public/assets/gate/cs/structure.json
            // parts: [.., .., public, assets, gate, cs, structure.json]

            // We can match "assets/<examId>/"
            // Or simpler, just regex it
            const match = normalizedPath.match(new RegExp(`/assets/${examId}/([^/]+)/structure.json$`))

            if (match) {
                const streamId = match[1]
                // We cannot read the file content (name/code) from the URL glob.
                // We rely on the folder name (streamId) for the ID and display name fallback.
                foundStreams.push({
                    id: streamId,
                    name: streamId.toUpperCase().replace(/-/g, ' '),
                    code: streamId
                })
            }
        }

        setStreams(foundStreams)
        setLoading(false)

    }, [examId])

    return { streams, loading }
}

export interface ExamInfo {
    id: string
    name: string
    description: string
}

// Re-use the same globs to infer available exams
export function useAvailableExams() {
    const [exams, setExams] = useState<ExamInfo[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        // We can deduce available exams by looking at the paths in structureGlobs
        // Path format: "../../public/assets/<examId>/<streamId>/structure.json"

        const foundExams = new Map<string, ExamInfo>()

        for (const path in structureGlobs) {
            // Normalize path separators
            const normalizedPath = path.replace(/\\/g, '/')
            // Regex to capture examId (index 1)
            const match = normalizedPath.match(/\/assets\/([^/]+)\/([^/]+)\/structure.json$/)

            if (match) {
                const examId = match[1]

                if (!foundExams.has(examId)) {
                    // Start with basic info from ID
                    // We attempt to fetch info.json but providing a fallback immediately
                    const name = examId.toUpperCase()
                    foundExams.set(examId, {
                        id: examId,
                        name: name,
                        description: `Best resources for ${name} preparation`
                    })
                }
            }
        }

        // Convert map to array
        const initialExams = Array.from(foundExams.values())
        setExams(initialExams)
        setLoading(false)

    }, [])

    return { exams, loading }
}
