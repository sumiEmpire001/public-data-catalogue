"""Validate and search metadata records for public datasets."""
import argparse
import json
from urllib.parse import urlparse


def validate(record):
    if not isinstance(record,dict):
        raise ValueError("dataset must be an object")
    for key in ("id","title","description","category","license","url"):
        if not isinstance(record.get(key),str) or not record[key].strip():
            raise ValueError("missing or invalid "+key)
    parsed=urlparse(record["url"])
    if parsed.scheme not in ("https","http") or not parsed.netloc:
        raise ValueError("invalid dataset URL")
    return record


def catalogue(records,query="",category="",license_name=""):
    if not isinstance(records,list):
        raise ValueError("catalogue must be a list")
    ids=set()
    matches=[]
    for record in records:
        validate(record)
        if record["id"] in ids:
            raise ValueError("duplicate dataset ID")
        ids.add(record["id"])
        search_text=" ".join(record[key] for key in ("title","description","category")).casefold()
        if query.casefold() not in search_text:
            continue
        if category and record["category"].casefold()!=category.casefold():
            continue
        if license_name and record["license"].casefold()!=license_name.casefold():
            continue
        matches.append(record)
    return sorted(matches,key=lambda item:item["title"].casefold())


def summary(records):
    validated=catalogue(records)
    categories={}
    for item in validated:
        categories[item["category"]]=categories.get(item["category"],0)+1
    return {"total":len(validated),"categories":dict(sorted(categories.items()))}


def main():
    parser=argparse.ArgumentParser(description="Search an offline dataset catalogue")
    parser.add_argument("file")
    parser.add_argument("--query",default="")
    parser.add_argument("--category",default="")
    parser.add_argument("--license",default="")
    args=parser.parse_args()
    with open(args.file,encoding="utf-8") as source:
        records=json.load(source)
    print(json.dumps({"summary":summary(records),"results":catalogue(records,args.query,args.category,args.license)},indent=2))


if __name__=="__main__":
    main()
