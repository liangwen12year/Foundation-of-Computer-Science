#include<iostream>
#include<string>
#include<vector>
#include <json/json.h>

using namespace std;


int main()
{
	Json::Value jsonRoot;
ifstream ifs; //��׼������
jsonRoot=ifs.open("sample.json");
for (auto i = 0; i < jsonRoot.size(); i++)//��������[]
{
	for (auto sub = jsonRoot[i].begin(); sub != jsonRoot[i].end(); sub++)//��������{}
	{
		cout << sub.name() << " : " << jsonRoot[i][sub.name()] << endl; //����1
		//cout << sub.name() << " : " << (*sub) << endl; //����2
	}
}

	return 0;
}

