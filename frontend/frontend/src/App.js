import Login from './Login';
import Browse from './Browse';
import { BrowserRouter, useState, Routes, Route } from "react-router-dom";
import SubUserSelect from './ChooseUser';

function App() {
  return (
    <BrowserRouter>
    <Routes>
    <Route path="/login" element={<Login />} />
    <Route path="/subuserselect" element={<SubUserSelect />} />
    <Route path="/browse" element = {<Browse />} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
