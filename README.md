Preview
<h1 align="center" id="title">Project Overview : Event 360 Backend</h1>

<p id="description">Event 360 is a comprehensive event management system designed to streamline the organization and management of various events. The system provides a platform for users to browse through different event categories access details about services offered view event items and explore recent events. Developed using Django and Django REST Framework Event 360 offers a robust backend architecture coupled with PostgreSQL database to ensure efficient data management and retrieval.</p>

<h2>🚀 Demo</h2>

[https://phero-l2-event-management-system.onrender.com/](https://phero-l2-event-management-system.onrender.com/)

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Event Categories: Browse and manage different event categories.
*   Services: Access information about services offered within each event category.
*   Event Items: View and manage event items associated with specific events.
*   Recent Events: Explore details about recent events including descriptions and images.
*   Authentication and Permissions: Secure access to the system with JWT authentication and define permissions for various actions.

<h2>🛠️ Setup Instructions:</h2>

<p>1. Ensure Python and Django are installed.</p>

```
Install required dependencies using " pip install -r requirements.txt " .
```

<p>2. Database Setup: Create a PostgreSQL database.</p>

 ```
 Update the database settings in settings.py with the database name user and 
 password.
 ```

<p>3. Running the Server:</p>

```
 Start the Django development server using " python manage.py runserver ".
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Django
*   Django REST Framework
*   PostgreSQL database

  
<h2> API Endpoints</h2>
<p>1. Service Endpoints :</p>

 * GET /service-list/
 * POST /create-service/
 * GET /service-list-by-category/
 * PUT /service-update/<service_id>/
 * DELETE /service-delete/<service_id>/
 
<p>2. Service Endpoints :</p>

* Event Items : Similar endpoints as Services for CRUD operations on Event Items.

<p>3. Service Endpoints :</p>

* Recent Events:Similar endpoints as Services for CRUD operations on Recent Events.

