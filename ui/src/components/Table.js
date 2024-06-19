import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHeart, faUpLong, faDownLong } from '@fortawesome/free-solid-svg-icons';
import '../styles/table.css';
import api from './api'
const Table = ({ data ,user,setPage}) => {
  const [colors, setColors] = useState({})

  useEffect(() => {
    if (data && data.length > 0) {
      const initialColors = data.reduce((acc, item) => {
        acc[item.id] = item.is_watchlisted;
        return acc;
      }, {});
      setColors(initialColors);
    }
  }, [data]);

  const handleToggleColor =  (index, stockId) => {
    document.getElementById(stockId).classList.add('fa-bounce')

    console.log('colors are',colors)
    // Use functional form of setColors to ensure updated state
    
     setColors((prevColors) => {
      const updatedColors = { ...prevColors };
      updatedColors[stockId] = !prevColors[stockId];
      return updatedColors;
    });
    setTimeout(() =>{
      document.getElementById(stockId).classList.remove('fa-bounce')
      api
      .post(`stocks/watchlist_modify`, {
        stockId: stockId,
        action: colors[stockId] ? 'remove' : 'add',
      })
      .then((res) => {
        setPage('home')
      })
      .catch((err) => alert(err));
      },500)
    // Use updatedColors immediately after setting state
    
  };
  return (
    <table className="table border border-dark">
      <thead style={{backgroundColor: 'rgba(229, 140, 155, 0.886)'}}>
        <tr>
          <th>S.N.O</th>
          <th>Symbol</th>
          <th>TimeZone</th>
          <th>Date & Time</th>
          <th>Open</th>
          <th>High &nbsp; <FontAwesomeIcon icon={faUpLong} bounce style={{ color: "#63E6BE" }} /></th>
          <th>Low &nbsp; <FontAwesomeIcon icon={faDownLong} bounce style={{ color: "#ff0000" }} /> </th>
          <th>Close</th>
          <th>Volume</th>
          <th>likes</th>
        </tr>
      </thead>
      <tbody>
        {data.length!==0 ? data.map((stock, index) => (
          <tr
            key={index}
            className="table-row"
          >
            <td>
              <span className="cell-content">{index + 1}</span>
            </td>
            <td>{stock.symbol}</td>
            <td>{stock.timezone}</td>
            <td>{stock.timestamp}</td>
            <td>{stock.open}</td>
            <td className='bg-success'>{stock.high}</td>
            <td className='bg-danger'>{stock.low}</td>
            <td>{stock.close}</td>
            <td>{stock.volume}</td>
            <td>
              <span role='button' className="heart-icon">
                
                <FontAwesomeIcon
                
                  size="2x"
                  color={stock.is_watchlisted ?'red' : 'white'} // true: red, false: white
                  icon={faHeart}
                  id={stock.id}
                  onClick={() => handleToggleColor(index,stock.id)}
                />
              </span>
            </td>
          </tr>
        )):<tr className='text-center'><td colspan="12">{user? 'No Watchlist added':'Please Sign in to see the Stocks '}</td> </tr>}
      </tbody>
    </table>
  );
};

export default Table;
