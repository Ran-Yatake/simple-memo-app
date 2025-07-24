'use client'

import { useEffect, useState } from 'react'
import axios from 'axios'

type Memo = {
  title: string
  content: string
}

export default function Home() {
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [memos, setMemos] = useState<Memo[]>([])

  const fetchMemos = async () => {
    try {
      const res = await axios.get<Memo[]>('http://localhost:5000/memo')
      setMemos(res.data)
    } catch (error) {
      console.error('メモの取得に失敗しました', error)
    }
  }

  const addMemo = async () => {
    try {
      await axios.post('http://localhost:5000/memo', {
        title,
        content,
      })
      setTitle('')
      setContent('')
      fetchMemos()
    } catch (error) {
      console.error('メモの保存に失敗しました', error)
    }
  }

  useEffect(() => {
    fetchMemos()
  }, [])

  return (
    <main style={{ padding: '2rem' }}>
      <h1>メモを追加</h1>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="タイトル"
        style={{ width: '100%', padding: '0.5rem', marginBottom: '1rem' }}
      />
      <br />
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="内容"
        style={{ width: '100%', height: '100px', padding: '0.5rem' }}
      />
      <br />
      <button onClick={addMemo} style={{ marginTop: '1rem' }}>
        保存
      </button>

      <h2>保存されたメモ</h2>
      <ul>
        {memos.map((memo, i) => (
          <li key={i}>
            📌 {memo.title}: {memo.content}
          </li>
        ))}
      </ul>
    </main>
  )
}
