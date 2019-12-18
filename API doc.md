# API document

[Imgur](https://i.imgur.com/9jC5bTN.png)

## View from Order

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

#### 1. Show the domain field of the project participants

**What is domain field**?

```code{Javascript}
GET 114.32.23.161/api/proj/?
```

**Server response:**

```code{Javascript}
To b configured
```

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

Use API with "PUT 114.32.23.161/api/proj", body being json object.

#### 1. Request for more resources

```code{Javascript}
{
    "Project_id": "Id 1",
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

#### Create Manager

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

#### 1. Show crews can be promoted

The term "promoted" seems ambiguous and needs somewhat more robust definitions. Hence, I define the action for this feature to be as follows.

The crew can be updated with some other "Job Title" and "salary".

```code{Javascript}
 114.32.23.161/api/crew/
```

**Server response:**

```code{Javascript}
To b configured
```

#### 2. Select certain Talents of the People

#### 3. Show the background, basic info for each person.

#### 4. Show what they are accountable for(Manage) or assigned to do(has a manager)

#### 5. Select Crew by Dev Team
