import React,{useState, useEffect} from 'react';
import { Card } from '../Components/Card/card';

export const TodoPage = ()=>{

    const [todo, setTodo] = useState([])

    useEffect(()=>{
        fetch('/api').then(response => {
            if (response.ok) {
                return response.json()
            }
        })
    },[])

    return(
        <>
            <Card/>
        </>
    )
}