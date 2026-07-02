import { useState } from 'react'

export default function TaskForm({ onCreate }) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  function handleSubmit(e) {
    e.preventDefault()
    if (!title.trim()) return
    onCreate({ title: title.trim(), description: description.trim() || undefined })
    setTitle('')
    setDescription('')
  }

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="What needs to be done?"
        className="task-input"
        autoFocus
      />
      <input
        type="text"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Add a description (optional)"
        className="task-input description-input"
      />
      <button type="submit" className="btn btn-primary" disabled={!title.trim()}>
        Add Task
      </button>
    </form>
  )
}