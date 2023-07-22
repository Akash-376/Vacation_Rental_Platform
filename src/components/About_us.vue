<template>
    <div class="about-us">
        <h1 class="heading">About Us</h1>
        <p class="description">
            Welcome to our vacation rental platform! We are dedicated to providing you with the best vacation experience,
            connecting you with stunning properties around the world. Our platform offers a wide range of properties for
            every
            taste and budget, whether you are a guest looking for a perfect vacation spot or a host eager to list your
            property. With our easy-to-use interface and seamless booking process, planning your dream vacation has never
            been
            easier.
        </p>
        <div class="team">
            <h2 class="team-heading">Our Team</h2>
            <div class="member">
                <img src="https://media.glamour.com/photos/56963389d9dab9ff41b53594/master/w_320%2Cc_limit/entertainment-2012-02-0206-15-import-dan-stevens-li.jpg"
                    alt="Member 1" class="member-image" />
                <div class="member-details">
                    <h3 class="member-name">John Doe</h3>
                    <p class="member-role">Co-founder & CEO</p>
                    <p class="member-contact">john@homes.com</p>
                    <p class="member-bio">
                        John is a visionary leader with a passion for travel. He believes that every traveler deserves a
                        memorable
                        and unique experience, and that's what drives our mission here at Vacation Rental Platform.
                    </p>
                </div>
            </div>
            <div class="member">
                <img src="https://qph.cf2.quoracdn.net/main-qimg-280e777f8565d2eb04e13ea5eaf525ad-lq" alt="Member 2"
                    class="member-image" />
                <div class="member-details">
                    <h3 class="member-name">Jane Smith</h3>
                    <p class="member-role">Co-founder & CTO</p>
                    <p class="member-contact">jane@homes.com</p>
                    <p class="member-bio">
                        Jane is a tech enthusiast and an expert in building scalable and user-friendly platforms. She
                        ensures that
                        our website is cutting-edge and always provides a seamless experience for our users.
                    </p>
                </div>
            </div>
            <div class="member">
                <img src="https://thumbs.dreamstime.com/b/happy-senior-business-man-smiling-portrait-45140025.jpg"
                    alt="Member 3" class="member-image" />
                <div class="member-details">
                    <h3 class="member-name">Michael Johnson</h3>
                    <p class="member-role">Founder</p>
                    <p class="member-contact">michael@homes.com</p>
                    <p class="member-bio">
                        Michael is the visionary behind our vacation rental platform. With years of experience in the travel
                        industry, he founded this platform with the goal of making vacations more enjoyable and hassle-free
                        for
                        everyone.
                    </p>
                </div>
            </div>
        </div>

        <div class="about-goals">
            <div class="goal" id="goal">Our Goals</div>
            <div class="goal">
                <i class="fas fa-globe"></i>
                <h3 class="goal-title">Global Reach</h3>
                <p class="goal-description">
                    Our primary goal is to connect travelers with beautiful vacation rentals around the globe. We aim to
                    provide a
                    diverse range of properties in various locations, ensuring that every traveler finds their dream
                    vacation spot.
                </p>
            </div>
            <div class="goal">
                <i class="fas fa-heart"></i>
                <h3 class="goal-title">Exceptional Experiences</h3>
                <p class="goal-description">
                    We are committed to offering exceptional travel experiences to our guests. From luxurious villas to cozy
                    cabins,
                    we curate properties that cater to every traveler's preferences, making their vacation truly memorable.
                </p>
            </div>
            <div class="goal">
                <i class="fas fa-hands-helping"></i>
                <h3 class="goal-title">Host Success</h3>
                <p class="goal-description">
                    Our platform is designed to support hosts in managing their vacation rentals efficiently. We provide
                    tools and
                    resources to enhance their listings, attract more guests, and ensure the success of their rental
                    business.
                </p>
            </div>
            <div class="goal">
                <i class="fas fa-comments"></i>
                <h3 class="goal-title">Customer Satisfaction</h3>
                <p class="goal-description">
                    Customer satisfaction is at the core of our mission. We strive to deliver exceptional customer service
                    and
                    respond promptly to any queries or concerns, ensuring that our guests have a stress-free and delightful
                    experience.
                </p>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'AboutUs'
}
</script>
  
<style scoped>
.about-us {
    padding: 20px;
    text-align: center;
}

.heading {
    font-size: 36px;
    margin-bottom: 20px;
}

.description {
    font-size: 18px;
    line-height: 1.6;
    margin-bottom: 30px;
}

.team {
    margin-top: 30px;
}

.team-heading {
    font-size: 24px;
    margin-bottom: 20px;
}

.member {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
}

.member-image {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin-right: 20px;
}

.member-details {
    text-align: left;
}

.member-name {
    font-size: 22px;
    margin-bottom: 10px;
}

.member-role {
    font-size: 18px;
    color: #888;
    margin-bottom: 3px;
}

.member-contact {
    font-size: 15px;
    color: #888;
    margin-bottom: 5px;
}

.member-bio {
    font-size: 16px;
    line-height: 1.6;
}



/* Styling for the Goals Section */
.about-goals {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    max-width: 1200px;
    margin: 0 auto;
    padding: 30px;
}

.section-heading {
    flex-basis: 48%;
    text-align: center;
    
}
#goal{
    font-size: 22px;
    font-weight: 900;
}

.goal {
    flex-basis: 48%;
    margin: auto;
    margin-bottom: 30px;
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 5px;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out;
}

.goal:hover {
    transform: translateY(-5px);
}
#goal:hover {
    transform: translateY(0);
}

.goal i {
    font-size: 24px;
    margin-bottom: 10px;
    color: #4CAF50;
}

.goal-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #333;
}

.goal-description {
    font-size: 16px;
    line-height: 1.6;
    color: #555;
}
</style>
  