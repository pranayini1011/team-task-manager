import { useEffect, useState } from "react";
import API from "../api";

function Tasks() {

  const [tasks, setTasks] = useState([]);

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {

    try {

      const response = await API.get("/tasks/");

      setTasks(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  const createTask = async () => {

    try {

      await API.post(
        `/tasks/?title=${title}&description=${description}&due_date=2026-05-20T10:00:00&priority=high&project_id=1&assigned_to=1`
      );

      alert("Task created");

      fetchTasks();

      setTitle("");
      setDescription("");

    } catch (error) {

      console.log(error);

      alert("Failed");
    }
  };

  const updateStatus = async (taskId, status) => {

    try {

      await API.patch(
        `/tasks/${taskId}/status?status=${status}`
      );

      fetchTasks();

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="page-container">

      <h1>Tasks</h1>

      <div className="card">

        <input
          className="input"
          placeholder="Task Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />

        <input
          className="input"
          placeholder="Task Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <button
          className="button"
          onClick={createTask}
        >
          Create Task
        </button>

      </div>

      {tasks.map((task) => (

        <div
          className="card"
          key={task.id}
        >

          <h3>{task.title}</h3>

          <p>{task.description}</p>

          <p>
            <strong>Status:</strong> {task.status}
          </p>

          <select
            className="input"
            value={task.status}
            onChange={(e) =>
              updateStatus(task.id, e.target.value)
            }
          >

            <option value="todo">
              To Do
            </option>

            <option value="inprogress">
              In Progress
            </option>

            <option value="done">
              Done
            </option>

          </select>

        </div>
      ))}

    </div>
  );
}

export default Tasks;