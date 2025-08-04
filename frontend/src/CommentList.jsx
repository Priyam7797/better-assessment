import React, { useState } from "react";

const CommentList = ({ comments, onDelete, onEdit }) => {
  const [editId, setEditId] = useState(null);
  const [editText, setEditText] = useState("");

  const startEdit = (id, text) => {
    setEditId(id);
    setEditText(text);
  };

  const cancelEdit = () => {
    setEditId(null);
    setEditText("");
  };

  const saveEdit = () => {
    onEdit(editId, editText);
    cancelEdit();
  };

  return (
    <div>
      {comments.length === 0 ? (
        <p>No comments yet.</p>
      ) : (
        comments.map((comment) => (
          <div key={comment.id} style={{ marginBottom: "10px" }}>
            <strong>Comment:</strong>
            {editId === comment.id ? (
              <>
                <input
                  value={editText}
                  onChange={(e) => setEditText(e.target.value)}
                />
                <button onClick={saveEdit}>Save</button>
                <button onClick={cancelEdit}>Cancel</button>
              </>
            ) : (
              <>
                <p>{comment.text}</p>
                <button onClick={() => startEdit(comment.id, comment.text)}>
                  Edit
                </button>
                <button onClick={() => onDelete(comment.id)}>Delete</button>
              </>
            )}
          </div>
        ))
      )}
    </div>
  );
};

export default CommentList;
