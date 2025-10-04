Commands
    - Docker


    - GIT


# Small Notes
Python → the environment itself (the interpreter + standard libraries) 🏢
Pip install → adds tools/packages into that environment 📦
Uvicorn → one of the tools/packages in that environment that can run your FastAPI app 🧑‍🍳
You could also add:
FastAPI → another tool/package in that environment that lets you build APIs.
Pydantic → another package to handle data validation.


## from pymongo import MongoClient
 - pymongo is the Python library that lets your Python app talk to MongoDB.
 - MongoClient is a class inside pymongo that you use to create a connection to a MongoDB server.
 - Think of it like a remote control for your database: it allows your Python code to send commands to MongoDB.

## client = MongoClient("mongodb://username:password@mongodb:27017/mydb")
 - This line connects your Python code to MongoDB.
 - After this line, client represents the active connection to the database server. You can now send queries through it.

## note_db = client.get_database()
 - get_database() gets the database you want to work with.
 - If you pass no argument, it defaults to the database specified in the connection string (noteappdb in your case).
 - db now represents your database


## Rule of thumb:
 - Root user (MONGO_INITDB_ROOT_*) → must use authSource=admin.
 - App-specific user created in your app DB → no need for authSource, simpler URL.



# backend to frontend connection with the use opf s3 and cloudfront
Got it! Let’s go step by step — in Fargate, you don’t manually “register” your tasks” like you would with EC2. ECS handles it via the service. Here’s how it works:
1️⃣ Create a Target Group
    Go to EC2 → Target Groups → Create target group
    Target type: IP (important for Fargate)
    Protocol / Port: HTTP / 8000 (the port your FastAPI container listens on)
    VPC: choose the VPC where your Fargate service runs
    Skip health check changes for now (defaults are fine)
    Create the target group
2️⃣ Create an ALB (if not already)
    Go to EC2 → Load Balancers → Create Load Balancer → Application Load Balancer
    Scheme: Internet-facing
    Listeners: 443 (HTTPS) + attach ACM certificate
    Availability zones: select the subnets your Fargate tasks will be in

3️⃣ Create Fargate Service & Link Target Group
    Go to ECS → Cluster → Create Service → Fargate
    Task Definition: your FastAPI container
    Load balancing: enable Application Load Balancer
    Listener port: 443 (or 80 → redirect to 443)
    Target group: select the one you created
    Finish creating the service

✅ ECS will now automatically register your running Fargate tasks with the target group. No manual registration needed.

4️⃣ Optional: CloudFront
    Point your frontend fetches to the ALB HTTPS endpoint
    Ensure your CloudFront origin is the ALB DNS name (HTTPS)
    This avoids the mixed-content error