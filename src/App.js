import { Link } from "react-router-dom";

function App() {
  return (
  <div>
  <h2>Github Pages</h2>
  <h3>Deploying React to Github</h3>
  </div>
  );
}

const About = () => {
 return ( 
 <div>
 <Link to="/">Home</Link>
 <h2>About Page</h2> 
 </div>
 );
}

export default About;
export default App;
