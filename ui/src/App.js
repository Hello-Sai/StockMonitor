import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import Table from './components/Table';
import Register from './components/Register'
import Login from './components/Login'
import { useEffect, useState } from 'react';
import Cookies from 'js-cookie'
import api from './components/api';
function App() {
  const [page,setPage] = useState('Home')
  const [stocks,setStocks] = useState([{}])
  const[currentUser,setCurrentUser] = useState(() => Cookies.get('userId')?true:false);
  useEffect(() =>
    {
      console.log(currentUser)
      currentUser && api.get('stocks/get_stocks_list',{
        headers:{
        'X-CSRFToken': Cookies.get('csrftoken')
      }
      })
     .then(function(res){
         console.log(res.data)
         setStocks(res.data)
     }).catch(function(error){
       console.log(error)
     })
   }
  ,[currentUser])
  // const [event,setEvent]= useState(false);
  // const [userId,setUserId]=useState(0)
  // const [username,setUsername]=useState('')

  
  // const toggleForm = () => {
  //   !EventForm ?setEventForm(true):setEventForm(false);
  // };
  
  // useEffect(()=>{
  //    {
  //    Cookies.get('id') && API.get('/user')
  //   .then(function(res){
  //       setUserId(Cookies.get('id'));
  //       setUsername(res.data.username)
  //       console.log(res.data)
  //       setState('events')
  //   }).catch(function(error){
  //     console.log(error)
  //   })
  // }},[currentUser])
  
  // const toggleEvents = () =>{
  //   setEvent(!event);
  //   API.get('/events').then(res =>{console.log(res.data)})
  // }
  const HandleLoginSubmit = async (e) =>{
    // e.preventDefault();
    e.preventDefault();
    await api.post('accounts/login',{
        headers:{
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      username:e.target.username.value,
      password:e.target.password.value
    }).then(res => {alert(res.data);setCurrentUser(true);setPage('Home')}).catch(err =>{
      
       alert(JSON.stringify(err.response))})

  }
  
  const HandleRegistrationSubmit = async (e) =>{
    e.preventDefault();
    await api.post('accounts/register',{
        headers:{
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      username:e.target.username.value,
      password:e.target.password.value
    }).then(res => {
      alert(res.data);
    }).catch(err =>{
      
       alert(err.response)})
  }
  const handleLogout = () =>{
    api.get(`accounts/logout`,{
      headers:{
      'X-CSRFToken': Cookies.get('csrftoken')
    }
      // withCredentials:true
    })
    .then(function(res){
      setCurrentUser(false);
      console.log(res.data);
      setPage('Home')
    
    }).catch(err =>setPage('Home') &&console.log(err));
  }

  return (
    <div>
      <Navbar currentUser={currentUser}  togglePage={(page) => setPage(page)}/>
      {currentUser ?
        (() => {
            switch (page){
              case "Home":
              return <Table data={stocks
                  // {id:1,symbol:2,low:1,high:5,open:2,close:10,volume:7,timezone:6,timestamp:2},
                  // {id:1,symbol:2,low:1,high:5,open:2,close:10,volume:7,timezone:6,timestamp:2}
              } />
              case "WatchList":
                return <Table user={currentUser} data={stocks.filter(data => data.is_watchlisted ===true)}  />
              case "Logout":
                return handleLogout();

            }})():(() => {
              switch(page){
                case "Home":
                  return <Table user={false} data={[]}/>
                case "Register":
                  return <Register onSubmit={HandleRegistrationSubmit}/>;
                case "Login":
                  return <Login onSubmit={HandleLoginSubmit}/>;
              }
            })()}
    </div>
  );
}

export default App;
