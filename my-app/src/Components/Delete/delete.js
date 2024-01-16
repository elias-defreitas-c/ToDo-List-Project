import React from 'react'
import { useNavigate } from "react-router-dom";
export const Delete = ({ id }) =>{
    const navigate = useNavigate()
    const deleteTodo = () =>{
        fetch(`/api/${id}`,{
            method: 'POST',
            body: JSON.stringify({
                id: id
            })
        }).then(response => response.json())
            .then(data => {
                console.log(data)
                navigate("/")
            })
    }
    return(
        <>
            <button onClick={deleteTodo}>Löschen</button>
        </>
    )
}