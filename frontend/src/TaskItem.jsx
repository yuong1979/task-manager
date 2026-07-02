import { useState } from 'react'

export default function TaskItem({ task, onUpdate, onDelete }) {
  const [editing, setEditing] = useState(false)
  const [title, setTitle] = useState(task.title)
  const [description, setDescription] = useState(task.description || '')

  function handleToggle() {
    onUpdate(task.id, { completed: !task.completed })
  }

  function handleSave() {
    if (!title.trim()) return
    onUpdate(task.id, { title: title.trim(), description: description.trim() || null })
    setEditing(false)
  }

  function handleCancel() {
    setTitle(task.title)
    setDescription(task.description || '')
    setEditing(false)
  }

  if (editing) {
    return (
      <li className="task-item editing">
        <div className="task-edit-form">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="edit-input"
            autoFocus
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="edit-textarea"
            rows={2}
            placeholder="Description (optional)"
          />
          <div className="edit-actions">
            <button onClick={handleSave} className="btn btn-sm btn-primary">Save</button>
            <button onClick={handleCancel} className="btn btn-sm">Cancel</button>
          </div>
        </div>
      </li>
    )
  }

  return (
    <li className={`task-item ${task.completed ? 'completed' : ''}`}>
      <label className="task-checkbox">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={handleToggle}
        />
        <span className="checkmark" />
      </label>
      <div className="task-body">
        <span className="task-title">{task.title}</span>
        {task.description && <span className="task-desc">{task.description}</span>}
      </div>
      <div className="task-actions">
        <button onClick={() => setEditing(true)} className="btn btn-sm" title="Edit">
          Edit
        </button>
        <button onClick={() => onDelete(task.id)} className="btn btn-sm btn-danger" title="Delete">
          Delete
        </button>
      </div>
    </li>
  )
}