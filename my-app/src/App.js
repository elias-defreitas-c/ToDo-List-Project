import logo from './images/logo.svg';
import './App.css';
import { TodoPage } from "./Pages/TodoPage";
import { Show } from "./Pages/Show";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
} from "react-router-dom";

function App() {
  return (
    <div className="App">
        <Router>
            <Routes>
                <Route exact path={'/'} element={<TodoPage />} />
                <Route path={'/:id'} element={<Show />} />
            </Routes>
        </Router>
    </div>
  );
}

export default App;
