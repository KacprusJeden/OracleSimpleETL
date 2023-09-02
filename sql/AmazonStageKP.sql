set SERVEROUTPUT ON;

create table CategoryMasterKP
(
	CategoryID int primary key,
	CategoryName varchar2(50) not null
);

create table ProductMasterKP
(
	PID	int primary key,
	Name varchar2(40) not null,
	Price number not null,
	CategoryID int not null,
    foreign key (CategoryID) references CategoryMasterKP(CategoryID)
);

create table CustomerMasterKP
(
	CID	int	primary key,
	Name varchar2(40) not null,
	City varchar2(50) not null
);

create table SalesKP
(
	PID	int	not null,
	CID	int	not null, 
	SaleDate date not null,
	QtySold	int	not null,
	SalesKPAmount number not null,
	DeliveryDate date,	
    foreign key (CID) references CustomerMasterKP(CID),
    foreign key (PID) references ProductMasterKP(PID)
);
