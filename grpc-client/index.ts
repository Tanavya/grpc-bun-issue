import { GrpcClient } from "./client";

const client = new GrpcClient();
await client.helloWorld();
