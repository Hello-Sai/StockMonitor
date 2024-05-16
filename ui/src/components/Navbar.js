// Navbar.js
import React, { useState } from 'react';

const Navbar = ({togglePage,switchTabs,currentUser}) => {
    const [activeItem, setActiveItem] = useState(null);

    const handleClick = (index,item) => {
        setActiveItem(index === activeItem ? null : index);
        togglePage(item)
    };

    const menuItems = currentUser ?["Home",'WatchList','Logout'] :['Home', 'Register', 'Login'] ;

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-white">
            <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul className="navbar-nav  ">
                    {menuItems.map((item, index) => (
                        <li
                            key={index}
                            className={`nav-item ${activeItem === index ? 'active' : ''}`}
                            onClick={() => handleClick(index,item)}
                        >
                            <a
                                href="#"
                                className="nav-link text-dark"
                                style={{ fontWeight: 'bolder' }}
                            >
                                {item}
                            </a>
                        </li>
                    ))}
                </ul>
            </div>
        </nav>
    );
};

export default Navbar;
