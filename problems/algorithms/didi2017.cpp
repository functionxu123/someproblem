//地下迷宫题
//http://www.cnblogs.com/SHERO-Vae/p/5882357.html
/*
题目描述
小青蛙有一天不小心落入了一个地下迷宫，小青蛙希望用自己仅剩的体力值P跳出这个地下迷宫。为了让问题简单，假设这是一个n*m的迷宫。迷宫每个位置为0或者1. 0代表这个位置有障碍物，
小青蛙到达不了这个位置；1代表小青蛙可以达到的位置。小青蛙初始在(0,0)位置。地下迷宫的出口在(0,m-1)(保证这两个位置都是1，并且保证一定有起点到终点可达的路径)。
小青蛙在迷宫中水平移动一个单位距离需要消耗1点体力值。向上爬一个单位距离需要消耗3个体力值，向下移动不消耗体力值。当小青蛙的体力值等于0时候还没有到达出口，小青蛙将无法逃离迷宫。
现在需要你帮助小青蛙计算出能否用今生的体力值跳出迷宫（即达到(0,m-1)的位置 

输入：

输入 n+1行：
第一行为3个整数n,m(3<=m,n<=10),P(1<=P<=100)
接下来的n行：
每行m个0或者1，以空格分隔
输出：
如果能逃离迷宫，则输出一行体力消耗最小的路径，输出格式见样例所示；如果不能逃离迷宫，则输出“Can not escape!”。
测试数据保证答案唯一
 输入例子：
4 4 10
1 0 0 1
1 1 0 1
0 1 1 1
0 0 1 1

输出例子：

[0,0],[1,0],[1,1],[2,1],[2,2],[2,3],[1,3],[0,3]
*/
#include <iostream>
#include <vector>

#define len 10
#define up_pow 3
#define lr_pow 1
#define dow_pow 0

using namespace std;

int n,m,p;  
int kep_pow[len][len];
int kep[len][len]={0};
int kep_pos[len][len];
//up 0  right 1  down 2  left 3

int update_around(int r, int c){//ret the shortest cost to end
	if (r==0 && c==m-1) {
		
		return 0;
	}

	int ret_pow=-1;//wait to return
	if (r>0 && kep[r-1][c]){
		if (kep_pow[r-1][c]==-1 || kep_pow[r][c]+up_pow<kep_pow[r-1][c]){
			kep_pow[r-1][c]=kep_pow[r][c]+up_pow;


			int tep=update_around(r-1,c);
			if (tep!=-1 && (tep+up_pow<ret_pow || ret_pow==-1)) {ret_pow=tep+up_pow; kep_pos[r][c]=0;}
		}
	}

	if (c<m-1 && kep[r][c+1]){
		if (kep_pow[r][c+1]==-1 || kep_pow[r][c]+lr_pow<kep_pow[r][c+1]){
			kep_pow[r][c+1]=kep_pow[r][c]+lr_pow;

			int tep=update_around(r,c+1);
			if (tep!=-1 && (tep+lr_pow<ret_pow || ret_pow==-1)) {ret_pow=tep+lr_pow; kep_pos[r][c]=1;}
		}
	}

	if (r<n-1 && kep[r+1][c]){
		if (kep_pow[r+1][c]==-1 || kep_pow[r][c]+dow_pow<kep_pow[r+1][c]){
			kep_pow[r+1][c]= kep_pow[r][c]+dow_pow;

			int tep=update_around(r+1,c);
			if (tep!=-1 && (tep+dow_pow<ret_pow || ret_pow==-1)) {ret_pow=tep+dow_pow; kep_pos[r][c]=2;}
		}
	}

	if (c>0 && kep[r][c-1]){
		if (kep_pow[r][c-1]==-1 || kep_pow[r][c]+lr_pow<kep_pow[r][c-1]){
			kep_pow[r][c-1]=kep_pow[r][c]+lr_pow;

			int tep=update_around(r,c-1);
			if (tep!=-1 && (tep+lr_pow<ret_pow || ret_pow==-1)) {ret_pow=tep+lr_pow; kep_pos[r][c]=3;}
		}
	}



	return ret_pow;
}


int main(){

	int i,j,k;
	cin>>n>>m>>p;


	for ( i=0;i<n;++i){
		for ( j=0;j<m;++j){
			cin>>kep[i][j];

			kep_pow[i][j]=-1;
			kep_pos[i][j]=-1;
		}
	}
	kep_pow[0][0]=0;

	//0->block  1->noblock
	//from (0,0)->(0,m-1)
	//move left or right need 1 power
	//move up need 3,move down don't need power

	int tep=update_around(0,0);
	
	if (tep>p) {
		cout<<"Can not escape!";
	}else{
		//cout<<tep;
		i=j=0;
		while(!(i==0 && j==m-1)){
			cout<<"["<<i<<","<<j<<"],";
			if (kep_pos[i][j]==0){ i-=1;}
			else if (kep_pos[i][j]==1){ j+=1;}
			else if (kep_pos[i][j]==2){ i+=1;}
			else if (kep_pos[i][j]==3){ j-=1;}
		}
		cout<<"["<<i<<","<<j<<"]";
	}
	return 0;
 }
