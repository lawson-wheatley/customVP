import Login from './Login';
import Browse from './Browse';
import { BrowserRouter, useState, Routes, Route } from "react-router-dom";
import SubUserSelect from './ChooseUser';
import Play from './Play';
import Search from './Search';

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/search" element = {<Search />} />
      <Route path="/login" element={<Login />} />
      <Route path="/subuserselect" element={<SubUserSelect />} />
      <Route path="/browse" element = {<Browse />} />
      <Route path="/play" element = {<Play />} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
