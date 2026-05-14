import { useEffect, useState } from "react";

import API from "../api";

function Dashboard() {

  const [data, setData] = useState({});

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard = async () => {

    try {

      const response = await API.get(
        "/dashboard/"
      );

      setData(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="page-container">

      <h1>Dashboard</h1>

      <div className="dashboard-grid">

        <div className="dashboard-card">

          <h2>Total Tasks</h2>

          <p>{data.total_tasks}</p>

        </div>

        <div className="dashboard-card">

          <h2>Todo</h2>

          <p>{data.todo}</p>

        </div>

        <div className="dashboard-card">

          <h2>In Progress</h2>

          <p>{data.in_progress}</p>

        </div>

        <div className="dashboard-card">

          <h2>Done</h2>

          <p>{data.done}</p>

        </div>

        <div className="dashboard-card">

          <h2>Overdue</h2>

          <p>{data.overdue}</p>

        </div>

      </div>

      <div
        className="card"
        style={{ marginTop: "30px" }}
      >

        <h2>Tasks Per User</h2>

        {data.tasks_per_user &&

          Object.entries(
            data.tasks_per_user
          ).map(([user, count]) => (

            <p key={user}>

              <strong>{user}</strong>: {count}

            </p>
          ))
        }

      </div>

    </div>
  );
}

export default Dashboard;