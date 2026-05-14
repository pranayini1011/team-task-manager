import { useEffect, useState } from "react";
import API from "../api";

function Projects() {

  const [projects, setProjects] = useState([]);

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {

    try {

      const response = await API.get("/projects/");

      setProjects(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  const createProject = async () => {

    try {

      await API.post(
        `/projects/?name=${name}&description=${description}&created_by=1`
      );

      alert("Project created");

      fetchProjects();

      setName("");
      setDescription("");

    } catch (error) {

      console.log(error);

      alert("Failed");
    }
  };

  return (

    <div className="page-container">

      <h1>Projects</h1>

      <div className="card">

        <input
          className="input"
          placeholder="Project Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          className="input"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <button
          className="button"
          onClick={createProject}
        >
          Create Project
        </button>

      </div>

      {projects.map((project) => (

        <div
          className="card"
          key={project.id}
        >

          <h3>{project.name}</h3>

          <p>{project.description}</p>

        </div>
      ))}

    </div>
  );
}

export default Projects;