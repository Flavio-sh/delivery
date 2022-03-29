import React from 'react';
import {BrowserRouter, Route, Routes } from "react-router-dom";
import Orders from "./Orders";
import Home from "./Home";
import Navbar from "./Navbar";

export default function AppRoutes() {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path={"/orders"} element={<Orders />} />
                <Route path={"/"} element={<Home />} />
            </Routes>
        </BrowserRouter>
    )
}

