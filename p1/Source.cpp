#include<iostream>
#include<string>
#include<vector>
#include <json/json.h>

using namespace std;


int main()
{
	Json::Value jsonRoot;
ifstream ifs; //标准输入流
jsonRoot=ifs.open("sample.json");
for (auto i = 0; i < jsonRoot.size(); i++)//遍历数组[]
{
	for (auto sub = jsonRoot[i].begin(); sub != jsonRoot[i].end(); sub++)//遍历对象{}
	{
		cout << sub.name() << " : " << jsonRoot[i][sub.name()] << endl; //方法1
		//cout << sub.name() << " : " << (*sub) << endl; //方法2
	}
}

	return 0;
}

