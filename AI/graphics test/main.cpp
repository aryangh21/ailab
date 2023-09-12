#include<graphics.h>
#include<bits/stdc++.h>
using namespace std;

int w1=10, h1=10, w2=60, h2=100, temp=1, filly=50;

void water_jug_bfs(int a, int b, int target);
void print_path(map<pair<int, int>, pair<int, int> > mp, pair<int, int> u, int a, int b);
void draw_jugs(int first, int second, int a, int b);

int main()
{
	int jug1, jug2, target;
    cout<<"Enter capacity of jug 1(Bigger jug): ";
    cin>>jug1;
    cout<<"Enter capacity of jug 2: ";
    cin>>jug2;
    cout<<"Enter target value to be measured: ";
    cin>>target;
    
    cout<<"Steps followed - \n";
    
    water_jug_bfs(jug1, jug2, target);
    
	return 0;
}

void water_jug_bfs(int a, int b, int target)
{
	//to avoid visiting same state again
    map<pair<int, int>, int> visited;
    bool isSolvable = false;
    
    //stores the path followed
    //pair 1 is achieved from pair 2
    map<pair<int, int>, pair<int, int> > mp;
 
    queue<pair<int, int> > q;
 
    q.push(make_pair(0, 0));
    while (!q.empty()) 
	{
        pair<int, int> u = q.front();
        q.pop();
        //if already visited
        if (visited[u] == 1)
            continue;
 
 		//redundant cases
        if ((u.first > a || u.second > b || u.first < 0 || u.second < 0))
            continue;
 
        visited[{ u.first, u.second }] = 1;
 
        if (u.first == target || u.second == target) 
		{
			//solution is found
            isSolvable = true;
 
 			//print path up until final state
 			initwindow(500, 4500, "Water Jug Problem");
            print_path(mp, u, a, b);
            //print final state
            if (u.first == target) 
			{
                if (u.second != 0)
                {
                	cout<<u.first<<" "<<0<<endl;
                	draw_jugs(u.first, 0, a, b);
				}
            }
            else 
			{
                if (u.first != 0)
                {
                	cout<<0<<" "<<u.second<<endl;
					draw_jugs(0, u.second, a, b);	
				}
            }
            getch();
            return;
        }
        
        //1. empty first jug
		//2. empty second jug
		//3. fill first jug
		//4. fill secong jug
		//5. transfer from first->second
		//6. transfer from second to first
        
        // completely fill the jug 2
        if (visited[{ u.first, b }] != 1) 
		{
            q.push({ u.first, b });
            mp[{ u.first, b }] = u;
        }
 
        // completely fill the jug 1
        if (visited[{ a, u.second }] != 1) 
		{
            q.push({ a, u.second });
            mp[{ a, u.second }] = u;
        }
 
        // transfer jug 1 -> jug 2
        int d = b - u.second;
        if (u.first >= d) 
		{
            int c = u.first - d;
            if (visited[{ c, b }] != 1) 
			{
                q.push({ c, b });
                mp[{ c, b }] = u;
            }
        }
        else 
		{
            int c = u.first + u.second;
            if (visited[{ 0, c }] != 1) {
                q.push({ 0, c });
                mp[{ 0, c }] = u;
            }
        }
        
        // transfer jug 2 -> jug 1
        d = a - u.first;
        if (u.second >= d) 
		{
            int c = u.second - d;
            if (visited[{ a, c }] != 1) 
			{
                q.push({ a, c });
                mp[{ a, c }] = u;
            }
        }
        else 
		{
            int c = u.first + u.second;
            if (visited[{ c, 0 }] != 1) 
			{
                q.push({ c, 0 });
                mp[{ c, 0 }] = u;
            }
        }
 
        // empty the jug 2
        if (visited[{ u.first, 0 }] != 1) 
		{
            q.push({ u.first, 0 });
            mp[{ u.first, 0 }] = u;
        }
 
        // empty the jug 1
        if (visited[{ 0, u.second }] != 1) 
		{
            q.push({ 0, u.second });
            mp[{ 0, u.second }] = u;
        }
    }
    if (!isSolvable)
    {
    	cout<<"No solution";
	}
}

void print_path(map<pair<int, int>, pair<int, int> > mp, pair<int, int> u, int a, int b)
{
	//find state that was before state(u) recursively
    if (u.first==0 && u.second==0)
	{
        cout<<0<<" "<<0<<endl;
        draw_jugs(0, 0, a, b);
        return;
    }
    print_path(mp, mp[u], a, b);
    cout<<u.first<<" "<<u.second<<endl;
    draw_jugs(u.first, u.second, a, b);
}

void draw_jugs(int first, int second, int a, int b)
{
	temp++;
	setcolor(WHITE);
	rectangle(w1, h1, w2, h2);
	if(first==a)
	{
		setfillstyle(SOLID_FILL, BLUE);
		floodfill(50, filly, WHITE);
	}
	setcolor(WHITE);
	rectangle(w1, (h1+(h2-h1)-(h2-h1)*first/a), w2, h2);
	if(first!=0 && first!=a)
	{
		setfillstyle(SOLID_FILL, BLUE);
		floodfill(50, (h1+((h2-h1)-(h2-h1)*first/a)+10), WHITE);
	}
	
	
	w1 += 80;
	w2 += 80;
	h1 += 20;
	
	setcolor(WHITE);
	rectangle(w1, h1, w2, h2);
	if(second==b)
	{
		setfillstyle(SOLID_FILL, BLUE);
		floodfill(100, filly, WHITE);
	}
	setcolor(WHITE);
	rectangle(w1, (h1+(h2-h1)-(h2-h1)*second/b), w2, h2);
	if(second!=0 && second!=b)
	{
		setfillstyle(SOLID_FILL, BLUE);
		floodfill(100, ((h1+(h2-h1)-(h2-h1)*second/b)+10), WHITE);
	}
	
	w1 -= 80;
	w2 -= 80;
	h1 += 100;
	h2 += 120;
	filly += 120;
}
