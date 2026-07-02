import { useState, useEffect } from 'react'
import TaskList from './TaskList'
import TaskForm from './TaskForm'
import './App.css'

export default function App() {
  const [tasks, setTasks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchTasks()
  }, [])

  async function fetchTasks() {
    try {
      const res = await fetch('/api/tasks')
      if (!res.ok) throw new Error('Failed to fetch tasks')
      const data = await res.json()
      setTasks(data)
      setError(null)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  async function handleCreate(data) {
    try {
      const res = await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
      if (!res.ok) throw new Error('Failed to create task')
      const task = await res.json()
      setTasks((prev) => [task, ...prev])
    } catch (err) {
      setError(err.message)
    }
  }

  async function handleUpdate(id, data) {
    try {
      const res = await fetch(`/api/tasks/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })
      if (!res.ok) throw new Error('Failed to update task')
      const updated = await res.json()
      setTasks((prev) => prev.map((t) => (t.id === id ? updated : t)))
    } catch (err) {
      setError(err.message)
    }
  }

  async function handleDelete(id) {
    try {
      const res = await fetch(`/api/tasks/${id}`, { method: 'DELETE' })
      if (!res.ok) throw new Error('Failed to delete task')
      setTasks((prev) => prev.filter((t) => t.id !== id))
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Task Manager</h1>
      </header>
      <main className="app-main">
        <TaskForm onCreate={handleCreate} />
        {error && <p className="error">{error}</p>}
        {loading ? (
          <p className="loading">Loading tasks...</p>
        ) : (
          <TaskList tasks={tasks} onUpdate={handleUpdate} onDelete={handleDelete} />
        )}
      </main>
    </div>
  )
}