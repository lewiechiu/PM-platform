
# API document
![](https://i.imgur.com/cQQ2fgX.png)

## View from Order

### Create

Use API with "POST 114.32.23.161/api/order/", body being json object.

#### 1. Create new Order
```code{Javascript}
{
    "established_time" : a string of time (Ex:"20191219"),
    "end_time" : a string of time (Initial value is 0),
    "deadline_time" : a string of time (Ex:"20200219"),
    "salesmanID" : id of salesman,
    "price" : int()
}
```
* Check if there is enough resource, such as Resource and SWE (no more than *k* cases per SWE) 
**-> need to add "estimated consumed resource" attri into the order table (Nick)**

### Read

Use API with "GET 114.32.23.161/api/order/..."

#### 1. View order priority

Input the top *k* orders from the data base. The priority of the orders are determined by the amount of price. For example, try to retrieve top 100 orders as shown below.

```code{Javascript}
GET 114.32.23.161/api/order/?top=100
```

**Server response:**

```code{Javascript}
{
    [
        {
            "order_id" : id of the order
            "established_time" : a string of time (Ex:"20191219"),
            "deadline_time" : a string of time (Ex:"20200219"),
            "salesmanID" : id of salesman,
            "price" : int()
       },
       {
            "order_id" : id of the order
            "established_time" : a string of time (Ex:"20191219"),
            ...
       },
    ]
    ...
}
```

#### 2. Know all projects which belongs to the order
Input the id of a order of which all child projects will be returned. Say, check the order of which id is 100.

```code{Javascript}
GET 114.32.23.161/api/order/?order_ID=100
```

**Server response:**


If the id you're looking for doesn't exist, it will throw an error at you.

```code{Javascript}
{
    [
        {
            "order_id" : [matches the id you search | none],
            "established_time" : a string of time (Ex:"20191219"),
            "deadline_time" : a string of time (Ex:"20200219"),
            "salesmanID" : id of salesman,
            "price" : int()
        },
        {
            "order_id" : [matches the id you search | none],
            "established_time" : a string of time (Ex:"20191219"),
            ... 
        }
    ]
}
```

#### 3. Know the salesman who is responsible for the order
Input the id of a order and the data of the salesman will be returned. Say, check the order of which id is 100.

```code{Javascript}
GET 114.32.23.161/api/order/?order_ID=100
```

**Server response:**
If the id you're looking for doesn't exist, it will throw an error at you.

```code{Javascript}
{
    [
        {
            "salesmanID" : [matches the id you search | none],
            "name" : string(name),
            "SSN" : a string (Ex:"521-25-8218"),
            "title" : string,
            "salary" : int(),
            "age" : int(),
            "year_of_experinece" : int() (Ex:"20200219"),
            "address" : a string of time (Ex:"20200219"),
            "gender" : str ing. "Male" | "Female"
        },
        {
            ... 
        }
    ]
}
```

#### 4. Know the current available capacity and personal


### Update

Use API with "PUT 114.32.23.161/api/order", body being json object.

#### 1. Modify an order’s project, ending date

```code{Javascript}
{
    "order_id": "Id 321",
    "end_time" : a string of time (Ex:"20201220". Initial value is 0),
    "salesmanID" : id of salesman,
    "price" : int(),
    ...
}
```


## View from Project Management

### Create

Use API with "POST 114.32.23.161/api/proj/", body being json object.

```code{Javascript}
{
    "Attr 1" : "Value 1",
    "Attr 2" : "Value 2",
    ...
}
```

1. Create new projects.
2. Create Task by customer feedback.

### Read

Use API with "GET 114.32.23.161/api/proj/..."

#### 2. Search active project (used by managers)

```code{Javascript}
GET 114.32.23.161/api/proj/active/
```

Internally, it will go through the database to see whether the task for a project has been done.

**Server Response:**

```code{Javascript}
{
    "No_id" : int(number of objects),
    "Projects" : [
        "Project_id1", "Project_id2", "Project_id3", ...
    ]
}
```

#### 3. Show team members’ domain fields

User needs to provide *team_id* for query. The following will get the id of team being "123"

```code{Javascript}
GET 114.32.23.161/api/proj/?team_id=123
```

**Server Response:**

```code{Javascript}
{
    {
        "name" : "name of the swe",
        "Job title" : "title",
        "Talent" : ["Talent1" ,"Talent 2", "Talent 3"]
    },
    {
        "name" : "name of the swe",
        "Job title" : "title",
        ...
    },
    ...
}
```

#### 4. Team Availability

```code{Javascript}
GET 114.32.23.161/api/proj/?team_id=123
```

**Server Response:**

```code{Javascript}
{
    [
        {
            "SWE_id" : id of the swe
            "name" : "name of the swe",
            "Available task" : int()
       },
       {
            "SWE_id" : id of the swe
            "name" : "name of the swe",
            ...
       },
    ]
    ...
}
```

### Update

Use API with "PUT 114.32.23.161/api/project/resources/<int:project_id>", body being json object.

#### 1. Request for more resources

```code{Javascript}
{
    "Resources" : [
        {
            "id" : "name of the resource",
            "amount" : int(amount needed)
        }, ...
    ]
    ...
}
```

#### 2. Update the state of the task

```code{Javascript}
{
    "Task_id": "Id",
    "state" : ["Complete" | "In Progress" | ...]
}
```

#### 3. Insert new SWE to the project

```code{Javascript}
{
    "Project_id": "Id",
    "SWE" : [
        {
            "id" : "id"
        },
        ...
    ]
}
```


## View from Crew

### Create

#### Create SWE

```code{Javascript}
POST 114.32.23.161/api/crew/swe
*** BODY ****
{
    "name" : char(name),
    "salary" : int(),
    "Job Title" : char(title),
    ...
}
```

#### Create Manager (TBD)

```code{Javascript}
POST 114.32.23.161/api/crew/manager
*** BODY ****
{
    "name" : char(name),
    "salary" : int(),
    "Job Title" : char(title),
    ...
}
```

### Read

#### 1. Show crews can be promoted (TBD: modify to show SWE's project experience)

The term "promoted" seems ambiguous and needs somewhat more robust definitions. Hence, I define the action for this feature to be as follows.

The crew can be updated with some other "Job Title" and "salary".

```code{Javascript}
 114.32.23.161/api/crew/
```

**Server response:**

```code{Javascript}
To b configured
```

#### 2. Select certain *Talents* of the People

```code{Javascript}
GET 114.32.23.161/api/crew/?talent="talent"
```

**Server response:**

```code{Javascript}
{
    [
        {
            "id" : employee id,
            "name" : name,
            "title" : title,
            some other fileds describing the worker.
        },
        {
            "id" : employee id,
            "name" : name,
            ...
        },
        ...
    ]
}
```

#### 3. Show the background, basic info for each person.

The following retrieves crew with ID being *123456*.

```code{Javascript}
GET 114.32.23.161/api/crew/?ID=123456
```

**Server response:**

If the id you're looking for doesn't exist, it will throw an error at you.

```code{Javascript}
{
    "id" : [matches the id you search | none],
    "name" : name,
    some other fields describing the worker...
}
```

#### 4. Show what they are accountable for(Manage) or assigned to do(has a manager)

**This is merged into the previous API**.

#### 5. Select Crew by Dev Team (TBD)

The following retrieves crew with ID being *123456*.

```code{Javascript}
GET 114.32.23.161/api/crew/?team_id=123456
```

**Server response:**

If the id you're looking for doesn't exist, it will throw an error at you.

```code{Javascript}
{
   "team_id" : [matches the id you search | none],
   "members" : [
       {
           "id" : id,
           "name" : name
       },
       {
           "id" : id,
           "name" : name
       },
       ...
   ]
}
```
