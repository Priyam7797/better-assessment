// src/App.jsx
import React, { useEffect, useState } from "react";
import CommentList from "./CommentList";
import CommentForm from "./CommentForm";
import api from "./api";

const App = () => {
  const [comments, setComments] = useState([]);

  const fetchComments = async () => {
    try {
      const response = await api.get("/comments/1"); // For Task ID 1
      console.log("Fetched comments data:", response.data);
      setComments(response.data);
    } catch (err) {
      console.error("Error fetching comments:", err);
    }
  };

  const addComment = async (newComment) => {
    try {
      const response = await api.post("/comments", {
        task_id: 1, // hardcoded task_id for now
        text: newComment,
      });
      console.log("Add comment response:", response.data);
      setComments([...comments, response.data]);
    } catch (err) {
      console.error("Error adding comment:", err);
    }
  };

  const deleteComment = async (id) => {
    try {
      await api.delete(`/comments/${id}`);
      setComments(comments.filter((comment) => comment.id !== id));
    } catch (err) {
      console.error("Error deleting comment:", err);
    }
  };

  const editComment = async (id, newText) => {
    try {
      await api.put(`/comments/${id}`, { text: newText });
      setComments(
        comments.map((comment) =>
          comment.id === id ? { ...comment, text: newText } : comment
        )
      );
    } catch (err) {
      console.error("Error editing comment:", err);
    }
  };

  useEffect(() => {
    fetchComments();
  }, []);

  return (
    <div className="container">
      <h1>Task Comments</h1>
      <CommentForm onSubmit={addComment} />
      <CommentList
        comments={comments}
        onDelete={deleteComment}
        onEdit={editComment}
      />
    </div>
  );
};

export default App;
