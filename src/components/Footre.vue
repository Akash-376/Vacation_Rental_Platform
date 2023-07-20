<template>
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h2>Contact Us</h2>
            <p>Email: contact@example.com</p>
            <p>Phone: +1 123-456-7890</p>
          </div>
          <div class="footer-section">
            <h2>Follow Us</h2>
            <div class="social-links">
              <a href="#" target="_blank" class="social-icon">
                <i class="fab fa-facebook"></i>
              </a>
              <a href="#" target="_blank" class="social-icon">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="#" target="_blank" class="social-icon">
                <i class="fab fa-instagram"></i>
              </a>
            </div>
          </div>
          <div class="footer-section">
            <h2>Useful Links</h2>
            <ul>
              <li><a href="#">Home</a></li>
              <li><a href="#">About Us</a></li>
              <li><a href="#">All Properties</a></li>
              <li><a href="#">Register as Host</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; {{ currentYear }} Your Vacation Rental. All rights reserved.</p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'FooterComp',
    data() {
      return {
        currentYear: new Date().getFullYear(),
      };
    },
  };
  </script>
  
  <style scoped>
  .footer {
    margin-top: 50px;
    background-color: #4b4b4b;
    color: #fff;
    padding: 30px 0;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .footer-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  
  .footer-section {
    padding: 10px;
  }
  
  .footer-section h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  .social-links {
    display: flex;
  }
  
  .social-icon {
    font-size: 1.2rem;
    color: #fff;
    margin-right: 10px;
  }
  
  .social-icon:hover {
    color: #00acee; /* Twitter color */
  }
  
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section li {
    margin-bottom: 5px;
  }
  
  .footer-section a {
    color: #fff;
    text-decoration: none;
  }
  
  .footer-bottom {
    text-align: center;
    padding-top: 20px;
    border-top: 1px solid #444;
  }
  
  .footer-bottom p {
    margin: 0;
  }
  
  </style>
  